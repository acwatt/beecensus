
# Documentation of the Google Earth Pro image-save config file (.geprint)


Variables from the config file below:
- save_image_quality: the resolution of the saved image. 
  - 0 = resolution of the window
  - 1 1024x768
  - 2 1280x720
  - 3 1920x1080
  - 4 3840x2160
  - 5 8192x4320
  - 6-9 4800x4800
  - 10+ nothing
    
- camera: tags that adjust the zoom and angle of the camera
    - `<gx:option enabled=\"0\" name=\"historicalimagery\">` makes the 
      historical imagery slider invisible.
      
    - `<longitude>, <latitude>` set the location
    - `<altitude>` is the distance from 
      ground
    - `<gx:altitudeMode>relativeToGround` changes the altitude from 
      sea-level to distance from ground
      
- `Layout\visible=false` turns off the overlay of the other map objects

```html
[General]
version=2
scaling_factor=1
print_type=0
print_quality=9
save_image_quality=6
print_flags=0
color_mode=0
camera=
"@ByteArray(<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<kml xmlns=\"http://www.opengis.net/kml/2.2\" xmlns:gx=\"http://www.google.com/kml/ext/2.2\" xmlns:kml=\"http://www.opengis.net/kml/2.2\" xmlns:atom=\"http://www.w3.org/2005/Atom\">
<Placemark>
	<LookAt>
		<gx:TimeStamp><when>2018-12-03</when>
		</gx:TimeStamp>
		<gx:ViewerOptions>
			<gx:option enabled=\"0\" name=\"historicalimagery\"></gx:option>
			<gx:option enabled=\"0\" name=\"sunlight\"></gx:option>
			<gx:option enabled=\"0\" name=\"streetview\"></gx:option>
		</gx:ViewerOptions>
		<longitude>-93.81981260476411</longitude>
		<latitude>30.75582863112696</latitude>
		<altitude>317</altitude>
		<heading>0</heading>
		<tilt>0</tilt>
		<range></range>
		<gx:altitudeMode>relativeToGround</gx:altitudeMode>
	</LookAt>
</Placemark>
</kml>
)"
[Title%20and%20Description]
Layout\size=@Size(248 84)
Layout\visible=false


[HTML%20Area]
Layout\size=@Size(393 96)
Layout\visible=false


[Legend]
Layout\size=@Size(175 154)
Layout\visible=false


[Scale]
Layout\size=@Size(360 20)
Layout\visible=false
Layout\anchor_pos=@Variant(\0\0\0\x1a?\xf0\0\0\0\0\0\0?\xf0\0\0\0\0\0\0)
Layout\anchor_halign=2
Layout\anchor_valign=2

[Compass]
Layout\size=@Size(72 72)
Layout\visible=false
Layout\anchor_pos=@Variant(\0\0\0\x1a?\xf0\0\0\0\0\0\0?\xef\x31\x8c`\0\0\0)
Layout\anchor_halign=2
Layout\anchor_valign=2

[Copyright]
Layout\size=@Size(152 40)
Layout\visible=false
Layout\anchor_pos=@Variant(\0\0\0\x1a\0\0\0\0\0\0\0\0?\xf0\0\0\0\0\0\0)
Layout\anchor_halign=0
Layout\anchor_valign=2

[Printer]
orientation=1
paper_size=3
```