
class Team:

  def __init__(self, name, abbr, slug):
    self.name = name
    self.abbr = abbr
    self.slug = slug

  def __repr__(self):
    return 'Team({0})'.format(self.name)

