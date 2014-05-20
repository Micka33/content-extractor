require 'psd'
require_relative 'util'
require_relative 'unit_manager'

class PandaPsd

  def initialize(file:nil)
    @errors = []
    @info = []
    @orientation = nil
    @unitManager = UnitManager.new
    @psd = PSD.new(file)
    @psd.parse!
  end

  attr_reader :info, :errors

  public

  def check_integrity
    check_dimensions
    self
  end

  def export
    @unitManager.export
  end

  def parse
    check_integrity
    go_through


    # #get an image
    # so = @psd.pget_layer_by_name('Smart Object (path d\'illustrator)')
    # so.pas_png
    #
    # #get a shape
    # so = @psd.pget_layer_by_name('Path rond')
    # so.pas_png
    #
    # #get a crop position
    # so = @psd.pget_layer_by_name('image croppée')
    # if so.phas_mask
    #   so.pas_png # get the whole image without cropping
    #   puts so.pget_mask_position
    # end
    #
    # #get a text
    # so = @psd.pget_layer_by_name('Texte')
    # if so.phas_text
    #   pp so.pget_text_html
    #   pp so.pget_positions
    #   pp so.pget_dimensions
    #   pp so.hidden?
    #   pp so.pvisible
    # end
    # puts UnitFactory::create_unit(so).as_json

    self
  end

  private

  def go_through
    return nil unless @errors.empty?
    @psd.tree.descendants_layers.each do |layer|
      @unitManager.create_unit(layer) if layer.pvisible_tree?
    end
  end

  def check_dimensions
    return nil unless @errors.empty?
    if @psd.pget_dimensions == [2048, 1536]
      @orientation = 'landscape'
    elsif @psd.pget_dimensions == [1536, 2048]
      @orientation = 'portrait'
    else
      @errors << 'Dimensions are wrong. Only 2048x1536 or 1536x2048.'
    end
  end

end



