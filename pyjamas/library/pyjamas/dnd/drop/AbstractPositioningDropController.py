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


from pyjamas.ui.Panel import Panel
from pyjamas.ui.Widget import Widget

"""*
* A {@link DropController} which allows a draggable widget to be placed at
* valid positions (locations) on the drop target, such as
* {@link com.google.gwt.user.client.ui.AbsolutePanel} or
* {@link com.google.gwt.user.client.ui.IndexedPanel}. Which positions are
* valid is determined by the implementing subclass.
"""
abstract class AbstractPositioningDropController extends AbstractDropController:
    String CSS_DRAGDROP_POSITIONER = "dragdrop-positioner"
    
    def __init__(self, dropTarget):
        super(dropTarget)
    
    
    """*
    * @deprecated No longer a part of the API.
    """
    def getPositioner(self):
        raise UnsupportedOperationException()
    
    
    """*
    * @deprecated No longer a part of the API.
    """
    def newPositioner(self, reference):
        raise UnsupportedOperationException()
    


