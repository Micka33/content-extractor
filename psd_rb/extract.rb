require 'psd'
require 'benchmark'
require 'pp'


module Panda
  module TreeUtil

    def get_layer_by_name(node, name)
      return nil unless @errors.empty?
      node.children_layers.map { |layer|
        return layer if layer.name == name
        nil
      }.compact.first
    end

  end

  module NodeUtil

    def is_foreground(node)
      node.group? && (node.name.downcase == @foreground_page_name)
    end

    def is_background(node)
      node.group? && (node.name.downcase == @background_page_name)
    end

    def is_visible(node)
      node.visible
    end

    def as_png(node, name:nil)
      return nil unless @errors.empty?
      name = node.name.gsub(/\s/, '_')+'.png' if name.nil? || name.empty?
      node.image.save_as_png './output/'+name
    end

    def has_mask(node)
      node.mask.size > 0
    end

  end

  class PsdUtil
    include TreeUtil
    include NodeUtil

    def initialize(file:nil)
      @foreground_page_name = 'foreground'
      @background_page_name = 'background'
    end


  end
end

class PandaPsd < Panda::PsdUtil

  def initialize(file:nil)
    @errors = []
    @info = []
    @orientation = nil
    @foreground = nil
    @background = nil
    @pages = []
    @psd = PSD.new(file)
    @psd.parse!
    super
  end

  attr_reader :info, :errors

  public

  def check_integrity
    check_dimensions
    self
  end

  def parse
    check_integrity
    # get_foreground; get_background; get_pages; go_through_pages

    #get an image
    so = get_layer_by_name(@psd.tree, 'Smart Object (path d\'illustrator)')
    pp "so.mask : #{so.mask.size == 0}"
    as_png(so)

    #get a crop position
    so = get_layer_by_name(@psd.tree, 'image croppée')
    pp "so.mask : #{so.mask.size == 0}"
    as_png(so) # get the whole image without cropping
    pp so.mask.instance_exec {[
        top-so.top,
        left-so.left,
        so.right-right,
        so.bottom-bottom
    ]}
    


    self
  end

  private

  def go_through_pages
    @pages.each do |page|
      page.children.each do |groups|
        pp groups.name
      end
    end
  end

  def get_foreground
    return nil unless @errors.empty?
    @psd.tree.children.each do |child|
      if is_foreground(child) && is_visible(child)
        @foreground = child
        break
      end
    end
    @info << 'No foreground page found.' if @foreground.nil?
  end

  def get_background
    return nil unless @errors.empty?
    @psd.tree.children.each do |child|
      if is_background(child) && is_visible(child)
        @background = child
        break
      end
    end
    @info << 'No background page found.' if @background.nil?
  end

  def get_pages
    return nil unless @errors.empty?
    # noinspection RubyResolve
    @psd.tree.children_groups.each do |child|
      @pages << child unless is_foreground(child) || is_background(child) || !is_visible(child)
    end
  end

  def check_dimensions
    return nil unless @errors.empty?
    if @psd.tree.document_dimensions == [2048, 1536]
      @orientation = 'landscape'
    elsif @psd.tree.document_dimensions == [1536, 2048]
      @orientation = 'portrait'
    else
      @errors << 'Dimensions are wrong. Only 2048x1536 or 1536x2048.'
    end
  end

end



Benchmark.bm(10) do |x|
  x.report('PandaPsd:') {
    # psd = PandaPsd.new(file:'./psds/rmn_v3.psd').parse
    psd = PandaPsd.new(file:'./psds/micka.psd').parse
    pp 'infos  -> '+psd.info.join(', ')
    pp 'errors -> '+psd.errors.join(', ')
  }
end
