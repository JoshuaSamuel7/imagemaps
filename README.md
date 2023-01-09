# Places Around Me
## AIM:
To develop a website to display details about the places around my house.

## Design Steps:

### Step 1:
Create a new django project and app
### Step 2:
Add a new imagemap html file in templates and neede images in static folder and define it in settings.
### Step 3:
Type ur image map code in the html with coordinates and target file to redirect on click
### Step 4:
Define your components pages and create content in such a way that it gives information about place which is being clicked
### Step 5:
Include pictures and contents for your subpages and map them using urls and views
## Code:
```
<!DOCTYPE html>
<html>
    <head>
        <title>Chennai Musuem Image Map</title>
    </head>
    <body>
        <h1 align='center'> Map Of Chennai Musuem</h1>
        <h2  align='left'>Address:</h2>
        <h3 align='left'>Government Maternity Hospital, Pantheon Rd, Egmore, Chennai, Tamil Nadu 600008</h3>
        <img src = "/static/images/map.jpg" height="750" width="800" align="center" usemap="#museummap">
        <map name="museummap">
            <area  alt="" title="Main Building" href="museum.html" shape="poly" coords="170,72,232,188,276,246,421,172,516,69,602,144,637,117,590,35,397,33,290,35" style="outline:none;" target="_self"     />
            <area  alt="" title="Botanical Garden" href="botanical.html" shape="poly" coords="595,213,690,409,696,486,745,464,741,210,733,168,712,125" style="outline:none;" target="_self"     />
            <area  alt="" title="Bronze Gallery" href="bronze.html" shape="poly" coords="114,280,370,628,543,526,243,235" style="outline:none;" target="_self"     />
            <area  alt="" title="Children's Museum" href="children.html" shape="poly" coords="104,624,242,780,382,667,242,530,246,511,235,499,377,649,223,524,244,506,242,525,204,499,282,797,378,704,387,688,408,663,198,535" style="outline:none;" target="_self"     />
            <area  alt="" title="Museum Theatre" href="theater.html" shape="poly" coords="359,304,520,219,651,396,686,483,638,536,566,496,513,482" style="outline:none;" target="_self"     />
        </map>
</body>
</html>
```

## Output:
![imagemap](imgmap/static/images/imagemap.jpg)

## Result:
Thus a website is developed to display details about the places around my house.