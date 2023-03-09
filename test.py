from DroneBlocksTelloSimulator import SimulatedDrone

if __name__ == '__main__':

    sim_key = '37a0b7a9-b1e0-4f47-9c41-c3a657503452'
    distance = 40

    drone = SimulatedDrone(sim_key)
    drone.takeoff()
    drone.fly_forward(distance, 'in')
    drone.fly_left(distance, 'in')
    drone.fly_backward(distance, 'in')
    drone.fly_right(distance, 'in')
    drone.flip_backward()
    drone.land()