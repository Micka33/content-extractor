class ImageUnit

  def initialize(node)
    @node = node
  end

  def type
    'ImageUnit'+( (@node.phas_crop)?(' with crop'):('') )
  end

  def to_json
    as_json
  end

  def as_json
    {
      stype: 'image',
      type: 'media',
      # flat_parent_ids: ["534f8f8e94da26c97d00002d"],
      # parent_ids: ["534f8f8e94da26c97d00002c"],
      # resource_ids: ["5347a61c5d04707f8f000059"],
      data: {
        isAutoName: false,
        world: {
          args: [536, 31, 329, 329, 0],
          width: 1024,
          height: 768,
          type: 'TMWorld'
        },
        unitName: @node.ppng_name,
        bindings: {
          ressources: nil,
          properties: {}
        },
        # indexChild: 2
      },
      _type: 'Unit'
    }
  end

end
