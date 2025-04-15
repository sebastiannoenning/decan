import sys, math, re
from enum import Enum
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QScrollArea, QLabel, QCheckBox, QSizePolicy, QDataWidgetMapper,
                               QScroller, QScrollerProperties, QStyleOption, QStyle)

""" ### Custom Scroller Functions for QT Modules
    #   -   PyQt Custom Functions that are expected to be reused
"""

# Function for creating a uni-directional scroller
def returnUniScroller(viewport: QScrollArea):
    """
    Convenience function for creating a uni-directional scroller

    Used like:
    yourScroller: QScroller = returnUniScroller(yourScrollArea: QScrollArea)

    Returns a scroller w/ properties applied enforcing uni-directional scroll rules.
       ↪ Properties are not expected to be changed, so internal is fine. 
       ↪ This can be enforced with high-axis lock, removal of overshooting and slight padding (1-2px) on the scrollable objects.
       ↪ Retains preset scroll properties; but will override the properties used for this effect
    """

    #   Create properties profile
    u_scroll = QScroller.scroller(viewport.viewport())
    u_scroll.grabGesture(viewport.viewport(), QScroller.ScrollerGestureType.LeftMouseButtonGesture)

    #   Set alternate properties profile to default
    u_scroll_properties = u_scroll.scrollerProperties()    # Copy preset properties ()

    # Remove Vertical Offshoot 
    u_scroll_properties.setScrollMetric(                                     
        QScrollerProperties.ScrollMetric.VerticalOvershootPolicy, 
        QScrollerProperties.OvershootPolicy.OvershootAlwaysOff)
    # Remove Horizontal Offshoot
    u_scroll_properties.setScrollMetric(                                   
        QScrollerProperties.ScrollMetric.HorizontalOvershootPolicy,
        QScrollerProperties.OvershootPolicy.OvershootAlwaysOff)  
    # Set uni-directional behaviour 
    u_scroll_properties.setScrollMetric(#                   Implement strong AxisLock (prevents bi-directional scroll movements)
        QScrollerProperties.ScrollMetric.AxisLockThreshold, # ↪ Value can be set between 0 & 1, with 1 indicating strong lock.
        1)             
    
    # Apply scroller properties to profile
    u_scroll.setScrollerProperties(u_scroll_properties)
    return u_scroll