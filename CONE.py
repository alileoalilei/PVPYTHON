from paraview.simple import *
# Create a cone and assign it as the active object
Cone()
# Set a property of the active object
SetProperties(Resolution=32)
# Apply the shrink filter to the active object
# Shrink is now active
Shrink() 
# Show shrink
Show() 
# Render the active view
Render() 
