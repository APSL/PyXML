from util import testAttribute
from util import testIntAttribute

def test():
    print 'testing source code syntax'
    from xml.dom.html import HTMLOListElement
    from xml.dom import implementation
    doc = implementation.createHTMLDocument('Title')
    o = doc.createElement('OL')

    print 'testing get and set'

    testIntAttribute(o,'compact')
    testIntAttribute(o,'start')
    testAttribute(o,'type')

    print 'get/set works'


if __name__ == '__main__':
    test()
