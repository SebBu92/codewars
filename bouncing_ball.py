def bouncing_ball(height, bounce, window):
    counter = 1
    if height > 0 and 0 < bounce < 1 and window < height:
        while height * bounce > window:
            height = height * bounce
            counter += 2
        print(counter)
    else:
        print(-1)


bouncing_ball(2, 0.5, 1)#, 1)
bouncing_ball(3, 0.66, 1.5)#, 3)
bouncing_ball(30, 0.66, 1.5)#, 15)
bouncing_ball(30, 0.75, 1.5)#, 21)