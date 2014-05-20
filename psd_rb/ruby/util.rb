
PSD.send(:define_method, 'pget_dimensions') do
  {width:tree.document_width, height:tree.document_height}
end

PSD.send(:define_method, 'pget_layer_by_name') do |name|
  tree.children_layers.map { |layer| return layer if layer.name == name }.compact.first
end


PSD::Node::Base.send(:define_method, 'pget_layer_by_name') do |name|
  children_layers.map { |layer| return layer if layer.name == name }.compact.first
end

PSD::Node::Base.send(:define_method, 'pget_dimensions') do
  {width:width, height:height}
end

PSD::Node::Base.send(:define_method, 'ppng_name') do
  name.gsub(/\s/, '_')+'.png'
end

PSD::Node::Base.send(:define_method, 'pas_png') do
  image.save_as_png '../output/'+ppng_name
end

PSD::Node::Base.send(:define_method, 'pis_group') do
  group?
end

PSD::Node::Base.send(:define_method, 'pvisible_tree?') do
  see_it = true
  see_it = visible? unless root?
  # noinspection RubyScope
  def rec(node, see_it)
    see_it = node.visible? unless node.root? || (!see_it)
    see_it = rec(node.parent, see_it) unless node.root? || (!see_it)
    see_it
  end
  see_it = rec(parent, see_it) unless root? || (!see_it)
  see_it
end

PSD::Node::Base.send(:define_method, 'pget_mask_position') do
  {
    top:    mask.top-top,
    left:   mask.left-left,
    right:  right-mask.right,
    bottom: bottom-mask.bottom
  }
end

PSD::Node::Base.send(:define_method, 'phas_mask') do
  (mask.size > 0)
end

PSD::Node::Base.send(:define_method, 'phas_crop') do
  phas_mask && (pget_mask_position != {top:0, left:0, right:0, bottom:0})
end

PSD::Node::Base.send(:define_method, 'phas_text') do
  text != nil
end

PSD::Node::Base.send(:define_method, 'pget_text') do
  text[:value] if phas_text
end

PSD::Node::Base.send(:define_method, 'pget_text_html') do
  '<TextFlow columnCount="1" columnGap="34" fontLookup="embeddedCFF" leadingModel="box" renderingMode="cff" textAlignLast="left" whiteSpaceCollapse="preserve" version="3.0.0" xmlns="http://ns.adobe.com/textLayout/2008">'+
    '<p lineHeight="135%" paragraphSpaceAfter="0" paragraphSpaceBefore="0">'+
      "<span color=\"##{'%02x%02x%02x' % text[:font][:colors].first[0, 3]}\" fontFamily=\"#{text[:font][:name]}\" fontSize=\"#{text[:font][:sizes].first}\">"+
      pget_text+
      '</span>'+
    '</p>'+
  '</textFlow>' if phas_text
end

PSD::Node::Base.send(:define_method, 'pget_positions') do
  {
    top:    top,
    left:   left,
    right:  right,
    bottom: bottom
  }
end











# module Panda

  # module TreeUtil
  #
  #   def get_layer_by_name(node, name)
  #     return nil unless @errors.empty?
  #     node = node.tree if node.instance_of?(PSD)
  #     # noinspection RubyResolve
  #     node.children_layers.map { |layer| return layer if layer.name == name }.compact.first
  #   end

  #   def get_dimensions(node)
  #     return nil unless @errors.empty?
  #     # noinspection RubyResolve
  #     return {width: node.tree.document_width, height: node.tree.document_height} if node.instance_of?(PSD)
  #     {width:node.width, height:node.height}
  #   end
  #
  # end

  # module NodeUtil

    # def is_visible(node)
    #   return nil unless @errors.empty?
    #   node.visible && !node.hidden?
    # end

    # def as_png(node, name:nil)
    #   return nil unless @errors.empty?
    #   name = node.name.gsub(/\s/, '_')+'.png' if name.nil? || name.empty?
    #   node.image.save_as_png './output/'+name
    # end

    # def has_mask(node)
    #   return nil unless @errors.empty?
    #   (node.mask.size > 0) && (get_mask_position(node) != {top:0, left:0, right:0, bottom:0})
    # end

    # def get_mask_position(node)
    #   return nil unless @errors.empty?
    #   node.mask.instance_exec {{
    #       top:    top-node.top,
    #       left:   left-node.left,
    #       right:  node.right-right,
    #       bottom: node.bottom-bottom
    #   }}
    # end

    # def has_text(node)
    #   return nil unless @errors.empty?
    #   node.text != nil
    # end

    # def get_text(node)
    #   return nil unless @errors.empty?
    #   node.text[:value]
    # end

    # def get_text_html(node)
    #   return nil unless @errors.empty?
    #   "<TextFlow columnCount=\"1\" columnGap=\"34\" fontLookup=\"embeddedCFF\" leadingModel=\"box\" renderingMode=\"cff\" textAlignLast=\"left\" whiteSpaceCollapse=\"preserve\" version=\"3.0.0\" xmlns=\"http://ns.adobe.com/textLayout/2008\">"+
    #       "<p lineHeight=\"135%\" paragraphSpaceAfter=\"0\" paragraphSpaceBefore=\"0\">"+
    #       "<span color=\"##{'%02x%02x%02x' % node.text[:font][:colors].first[0, 3]}\" fontFamily=\"#{node.text[:font][:name]}\" fontSize=\"#{node.text[:font][:sizes].first}\">"+
    #       get_text(node)+
    #       "</span>"+
    #       "</p>"+
    #       "</textFlow>"
    # end

    # def get_positions(node)
    #   return nil unless @errors.empty?
    #   node.instance_exec {{
    #       top:    top,
    #       left:   left,
    #       right:  right,
    #       bottom: bottom
    #   }}
    # end

  # end

  # class PsdUtil
  #   # include TreeUtil
  #   # include NodeUtil
  #
  #   def initialize(file:nil)
  #     @foreground_page_name = 'foreground'
  #     @background_page_name = 'background'
  #   end
  #
  #
  # end
# end