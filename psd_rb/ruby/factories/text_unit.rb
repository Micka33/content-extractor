class TextUnit

  def initialize(node)
    @node = node
  end

  def type
    'TextUnit'
  end

  def to_json
    as_json
  end

  def as_json
    {
      stype: 'Text',
      type: 'media',
      # flat_parent_ids: ["534f8f8e94da26c97d00002d"],
      # parent_ids: ["534f8f8e94da26c97d00002c"],
      # resource_ids: ["534f8f8e94da26c97d00002b"],
      data: {
        opacity: 0.5,
        world: {
          args: [160, 31, 200, 183, 0],
          width: 1024,
          height: 768,
          type: 'TMWorld'
        },
        unitName: @node.pget_text,
        bindings: {
          ressources: nil,
          properties: {}
        },
        # indexChild: 1
      },
      _type: 'Unit'
    }
  end
end
