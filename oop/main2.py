#define multiple constructors

class Hello:
    def __init__(self, name) : pass
    def __init__(self) : pass
    
hello = Hello('name')


class Hello:
    def __init__(self, *args, **kwargs) : pass
    def __init__(self) : pass
    
hello = Hello('name')
hello = Hello('name', 'ah', 'dddd', name = 'yasmine')
