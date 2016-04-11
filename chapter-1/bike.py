class Bike:
    #constructor
    def __init__(this, color, frame_material):
        this.color = color
        this.frame_material = frame_material
        
    #always provide self
    def brake(this):
        print("Breaking!", this.frame_material)
        
#let's create a couple of instances
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

print(red_bike)
print(red_bike.color)
print(red_bike.frame_material)

print(blue_bike)
print(blue_bike.color)
print(blue_bike.frame_material)

red_bike.brake();
blue_bike.brake();

exit()