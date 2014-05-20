class GroupUnit

  def initialize(node)
    @node = node
  end

  def type
    'GroupUnit'
  end

  def to_json
    as_json
  end

  def as_json
    {
      created_at: '2014-05-19T12:53:31Z',
      _id: '5379feb120d5ac429400004a',
      stype: 'group',
      flat_parent_ids: ['534f8f8e94da26c97d00002d'],
      data: {
        stacks: {
          '5379feb120d5ac429400004b'=> {
            ref: null,
            units: [0, 1],
            actions: {},
            thumb: nil,
            name: 'Untitled'
          },
          o: ['5379feb120d5ac429400004b']
        },
        world: {
          args: [243, 511, 321, 188, 0],
          width: 1024,
          height: 768,
          type: 'TMWorld'
        },
        unitName: 'Group_5774',
        indexChild: 3,
        internalWPid: '5379feb120d5ac429400004c'
      },
      flat_child_ids: %w(5379feb120d5ac429400004e 5379feb120d5ac429400004f),
      type: 'container',
      parent_ids: ['534f8f8e94da26c97d00002c'],
      sid: '534f8f8e94da26c97d00003a',
      updated_at: '2014-05-19T12:53:31Z',
      _type: 'Unit'
    }
  end
end