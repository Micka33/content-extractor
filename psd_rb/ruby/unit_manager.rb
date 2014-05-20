require_relative 'factories/unit_factory'

class UnitManager

  def initialize
    @units = []
  end
  attr_reader :units

  def create_unit(layer)
    unit = UnitFactory::create_unit(layer)
    @units << unit
    unit
  end

  def export
    @units.map{|unit| unit.as_json}
  end

end
