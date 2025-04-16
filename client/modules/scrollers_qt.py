import sys, math, re
from enum import Enum
from PySide6.QtCore import (Qt, 
                            QEasingCurve)
from PySide6.QtWidgets import (QScrollArea, QLabel, QCheckBox, QSizePolicy, QDataWidgetMapper,
                               QScroller, QScrollerProperties, 
                               QStyleOption, QStyle)

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
    u_scroll.grabGesture(
        viewport.viewport(), 
        QScroller.ScrollerGestureType.LeftMouseButtonGesture
        )

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


def returnDragScroller(viewport: QScrollArea):
    """
    Convenience function for creating a 'drag' scroller

    Used like:
    yourScroller: QScroller = returnDragScroller(yourScrollArea: QScrollArea)

    Returns a scroller w/ properties applied enforcing uni-directional scroll rules & also drag-scrolling.
       ↪ Properties are not expected to be changed, so internal is fine. 
       ↪ This can be enforced with high-axis lock, removal of overshooting and slight padding (1-2px) on the scrollable objects.
       ↪ Retains preset scroll properties; but will override the properties used for this effect
    """
    #   Create properties profile
    d_scroll = QScroller.scroller(viewport.viewport())
    d_scroll.grabGesture(
        viewport.viewport(), 
        QScroller.ScrollerGestureType.LeftMouseButtonGesture
        )

    #   Set alternate properties profile to default
    d_scroll_properties = d_scroll.scrollerProperties()    # Copy default properties

    d_scroll_properties.setScrollMetric(                                   
        QScrollerProperties.ScrollMetric.VerticalOvershootPolicy, 1)  
    d_scroll_properties.setScrollMetric(                                
        QScrollerProperties.ScrollMetric.HorizontalOvershootPolicy, 1)
    d_scroll_properties.setScrollMetric(                                      
        QScrollerProperties.ScrollMetric.AxisLockThreshold, 1)
    
    d_scroll_properties.setScrollMetric(
        QScrollerProperties.ScrollMetric.ScrollingCurve, QEasingCurve(QEasingCurve.Type.OutExpo))
    d_scroll_properties.setScrollMetric( #DecelerationFactor is a percentage decrease of velocity every frame
        QScrollerProperties.ScrollMetric.DecelerationFactor, 0.01) #I.e, around 0.5% each frame
    d_scroll_properties.setScrollMetric( # at 60 frames per second
        QScrollerProperties.ScrollMetric.FrameRate, QScrollerProperties.FrameRates.Fps60)
    d_scroll_properties.setScrollMetric(
        QScrollerProperties.ScrollMetric.MaximumVelocity, 0.635)
    
    d_scroll_properties.setScrollMetric(
        QScrollerProperties.ScrollMetric.SnapPositionRatio,0.33)
    """d_scroll_properties.setScrollMetric(
        QScrollerProperties.ScrollMetric.SnapTime())"""

    d_scroll_properties.setScrollMetric(
        QScrollerProperties.ScrollMetric.OvershootDragResistanceFactor, 0.33)
    d_scroll_properties.setScrollMetric(
        QScrollerProperties.ScrollMetric.OvershootScrollDistanceFactor, 0.33)
    
    d_scroll_properties.setScrollMetric(
        QScrollerProperties.ScrollMetric.DragStartDistance, 0.001)
    
    d_scroll.setScrollerProperties(d_scroll_properties)    #Set scroller properties to profile
    return d_scroll