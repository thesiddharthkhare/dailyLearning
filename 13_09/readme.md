Margin

margin: margin-top  margin-right  margin-bottom  margin-left
margin: 10px 20px 30px 40px;

margin: top&bottom    left&right
margin: 20px 0px;

Properties of box model:
Content: HTML Content =>
Padding: Space around the content within the border
Border: Area including content and padding
Margin: Not able to see any background color => space outside the border

div => Multiple classes
div => box and box1
div class="box box1"

1100px screen size => 250px width for each box => 4boxes
100px
24%

1300px screen size => proportionate => 250px for each box => very large space towards the right end 300px
24%

###
width and height and border
width => in terms of %
height => after creating the layout => remove height
content height
###


img => inline => width ??? => width of content => center align
convert img => block => fixed width => center align

p => block => width => screen width

Box Sizing
    box sizing: content-box;

default value

width: 200px;
padding: 50px;
margin: 50px;
height: 200px;
border: 2px solid blue;
box-sizing: border-box;

content-box =>
width = 200px, height=200px, padding=50px, margin=50px
200px + 50px + 50px + 2px + 2px = 304px

border-box => total width=200px => cotent width + padding width + border width
200px => 100px for padding, 4px for border => content width = 96px
