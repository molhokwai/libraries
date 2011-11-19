"""
* Copyright 2007 Fred Sauer
*
* Licensed under the Apache License, Version 2.0 (the "License"); you may not
* use this file except in compliance with the License. You may obtain a copy of
* the License at
*
* http:#www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
* WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
* License for the specific language governing permissions and limitations under
* the License.
"""


from pyjamas.ui.Widget import Widget

"""*
* Class to represent a rectangular region of a widget relative to another
* widget. Also keeps track of the size of the widget borders and its inner
* width and height.
"""
class WidgetArea extends AbstractArea:
    """*
    * Determine the area of a widget relative to a panel. The area returned is
    * such that the following are True:
    * <ul>
    * <li><code>parent.add(widget, area.getLeft(), area.getTop())</code>
    * leaves the object in the exact same location on the screen</li>
    * <li><code>area.getRight() = area.getLeft() + widget.getOffsetWidget()</code></li>
    * <li><code>area.getBottom() = area.getTop() + widget.getOffsetHeight()</code></li>
    * </ul>
    *
    * Note that boundaryPanel need not be the parent node, or even an ancestor of
    * widget. Therefore coordinates returned may be negative or may exceed the
    * dimensions of boundaryPanel.
    *
    * @param widget the widget whose area we seek
    * @param reference the widget relative to which we seek our area. If
    *            <code>None</code>, then <code>RootPanel().get()</code> is
    *            assumed
    """
    def __init__(self, widget, reference):
        int left = widget.getAbsoluteLeft()
        int top = widget.getAbsoluteTop()
        
        if reference is not None:
            left -= reference.getAbsoluteLeft()
            left -= DOMUtil.getBorderLeft(reference.getElement())
            top -= reference.getAbsoluteTop()
            top -= DOMUtil.getBorderTop(reference.getElement())
        
        int right = left + widget.getOffsetWidth()
        int bottom = top + widget.getOffsetHeight()
        setLeft(left)
        setTop(top)
        setRight(right)
        setBottom(bottom)
    


