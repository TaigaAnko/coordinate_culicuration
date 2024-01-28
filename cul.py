import math

def coordinate_cul(x, y, theta, x_0, y_0) -> None:
    def _theta_cal(x, y, theta):
        radians = math.radians(theta)
        ax = x * math.cos(radians) - y * math.sin(radians)
        ay = x * math.sin(radians) + y * math.cos(radians)
        print(ax, ay)
        
        return ax, ay
    
    ax, ay = _theta_cal(x, y ,theta)
    print(x_0, y_0)
    for _ in range(1, 11):
        x_0 += ax
        y_0 += ay
        print(x_0, y_0)


if __name__ == '__main__':
    coordinate_cul(0, 1.3, 10, 10, 10)