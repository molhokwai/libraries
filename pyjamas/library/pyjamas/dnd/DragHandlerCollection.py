"""
* Copyright 2008 Fred Sauer
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
* Helper class for controllers that accept
* {@link com.allen_sauer.gwt.dnd.client.DragHandler DragHandlers}. This
* subclass of ArrayList assumes that all items added to it will be of type
* {@link com.allen_sauer.gwt.dnd.client.DragHandler}.
"""
class DragHandlerCollection(ArrayList):
    """*
    * @deprecated Use {@link #fireDragEnd(DragEndEvent)} instead.
    """
    def fireDragEnd(self, context):
    
    
    """*
    * Fires a {@link DragHandler#onDragEnd(DragEndEvent)} on all handlers in the
    * collection.
    *
    * @param dragEndEvent the event
    """
    def fireDragEnd(self, dragEndEvent):
        for Iterator it = iterator(); it.hasNext();:
            handler = it.next()
            handler.onDragEnd(dragEndEvent)
        
    
    
    """*
    * @deprecated Use {@link #fireDragStart(DragStartEvent)} instead.
    """
    def fireDragStart(self, context):
    
    
    """*
    * Fires a {@link DragHandler#onDragStart(DragStartEvent)} on all handlers in
    * the collection.
    *
    * @param dragStartEvent the event
    """
    def fireDragStart(self, dragStartEvent):
        for Iterator it = iterator() it.hasNext():
            handler = it.next()
            handler.onDragStart(dragStartEvent)
        
    
    
    """*
    * @deprecated Use {@link #fireDragStart(DragStartEvent)} instead.
    """
    def fireDragStart(self, sender):
        raise UnsupportedOperationException()
    
    
    """*
    * @deprecated Use {@link #firePreviewDragEnd(DragEndEvent)} instead.
    """
    def firePreviewDragEnd(context):
		raise VetoDragException
    
    
    """*
    * Fires a {@link DragHandler#onPreviewDragEnd(DragEndEvent)} on all handlers
    * in the collection.
    *
    * @param dragEndEvent the event
    * @throws VetoDragException if the proposed operation is unacceptable
    """
    def firePreviewDragEnd(dragEndEvent):# throws VetoDragException
        for Iterator it = iterator(); it.hasNext();:
            handler = (DragHandler) it.next()
            handler.onPreviewDragEnd(dragEndEvent)
        
    
    
    """*
    * @deprecated Use {@link #firePreviewDragEnd(DragEndEvent)} instead.
    """
    def firePreviewDragEnd( sender, dropTarget)# throws VetoDragException
        raise UnsupportedOperationException()
    
    
    """*
    * @deprecated Use {@link #firePreviewDragStart(DragStartEvent)} instead.
    """
    void firePreviewDragStart(DragContext context) throws VetoDragException {
    
    
    """*
    * Fires a {@link DragHandler#onPreviewDragStart(DragStartEvent)} on all
    * handlers in the collection.
    *
    * @param dragStartEvent the event
    * @throws VetoDragException if the proposed operation is unacceptable
    """
    void firePreviewDragStart(DragStartEvent dragStartEvent) throws VetoDragException {
        for Iterator it = iterator(); it.hasNext();:
            DragHandler handler = (DragHandler) it.next()
            handler.onPreviewDragStart(dragStartEvent)
        
    
    
    """*
    * @deprecated Use {@link #firePreviewDragStart(DragStartEvent)} instead.
    """
    void firePreviewDragStart(Widget sender) throws VetoDragException {
        raise UnsupportedOperationException()
    


