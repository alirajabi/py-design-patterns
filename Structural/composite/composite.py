#!/usr/bin/env python
# GuiWindow is the Component in the composite design pattern

class GuiElement():
    
    def __init__(self, name):
        self.name = name
        self.parent = None

    # This should raise an error by default, since the Leaf classes
    # don't need to implement child addition and the composites will
    # implement the functionality.
    def add_child(self, component):
       print('Vanilla add_child called! this is most likely an error') 

    # get_children yields an empty list by default. Composites will
    # override this behavior.
    def get_children(self):
        return
        yield

    def draw(self):
        pass

    def identify(self):
        return '{} of type {}'.format(self.name, self.__class__.__name__)


# GuiComposite is the Composite type
class GuiComposite(GuiElement):
    
    def __init__(self, name):
        super().__init__(name)
        self.children = []
    
    # This is the only place where a component's parent is set.
    # It is good and it is intended.
    def add_child(self, component):
        component.parent = self
        self.children.append(component)
    
    def get_children(self):
        for child in self.children:
            yield child

    def draw(self):
        print("{} drawing it's children".format(self.identify()))
        for child in self.get_children():
            child.draw()
        print()
    

# GuiLeaf is the Leaf in the composite design pattern hierarchy
class GuiLeaf(GuiElement):
    
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print('{} (a(n) {}) is drawing itself'.format(self.name, self.__class__.__name__))


class GuiList(GuiComposite):
    def __init__(self, name):
        super().__init__(name)

class GuiDrawingPane(GuiComposite):
    def __init__(self, name):
        super().__init__(name)

class GuiText(GuiLeaf):
    def __init__(self, name):
        super().__init__(name)

class GuiPicture(GuiLeaf):
    def __init__(self, name):
        super().__init__(name)

class GuiButton(GuiLeaf):
    def __init__(self, name):
        super().__init__(name)


class BeautifulIterator():
    
    def __init__(self, gui_element):
        self.head = gui_element

    def iterate(self):
        self.iterate_utility(self.head, 0)

    def iterate_utility(self, node, depth):
        print('\t'*depth + node.identify())
        for child in node.get_children():
            self.iterate_utility(child, depth + 1)
        print()


def main():
    #main window 
    window = GuiDrawingPane('Main window')
   
    #layout
    panel = GuiDrawingPane('Left panel')
    text_list = GuiList('Rght side list')
    footer = GuiDrawingPane('footer')
    list_of_posts = GuiList('Posts')
   
    # adding links to text list
    for hyperlink in [GuiText('hyper link'), 
                      GuiText('hyperer link'),
                      GuiText('Absolutely mega ultra hyper link')]:
        text_list.add_child(hyperlink)
    
    window.add_child(text_list)
    
    # creating a post with a picture
    post1 = GuiDrawingPane('cool post')
    post1.add_child(GuiText('[insert cool title here]'))
    post1.add_child(GuiPicture('cool picture'))
    post1.add_child(GuiButton('Like!'))

    # creating a post with multiple texts
    post2 = GuiDrawingPane('boring post')
    post2.add_child(GuiText('text'))
    post2.add_child(GuiText('more text'))
    post2.add_child(GuiText('even more text'))
    post2.add_child(GuiButton('Dislike!'))
    
    # adding the constructed posts to the list
    list_of_posts.add_child(post1)
    list_of_posts.add_child(post2)

    panel.add_child(list_of_posts)
    
    window.add_child(panel)
    
    window.draw()

    BeautifulIterator(window).iterate()

if __name__ == '__main__':
    main()
