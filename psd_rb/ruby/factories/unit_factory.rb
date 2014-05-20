require_relative 'text_unit'
require_relative 'image_unit'
require_relative 'group_unit'
require_relative 'unknown_unit'

class UnitFactory

  def self.create_unit(node)
    if node.phas_text
      return TextUnit.new(node)
    elsif node.pis_group
      return GroupUnit.new(node)
    else
      return ImageUnit.new(node)
    end
  end

end
