from .field import *


def look_back(field, velocity_field, dt):
    """
Semi-Lagrangian advection with simple backward lookup.
    :param field: Field to be advected
    :param velocity_field: Field, need not be compatible with field.
    :param dt: time step
    :return: Field compatible with input field
    """
    try:
        x0 = field.sample_points
        v = velocity_field.resample(field)
        x = x0 - v * dt
        data = field.resample(x).data
        return field.copied_with(data=data)
    except StaggeredSamplePoints:
        advected = [look_back(component, velocity_field, dt) for component in field.unstack()]
        return field.copied_with(data=tuple(advected))


# def points(point_cloud, velocity_field, dt):
#     pass


# def dynamic(field, velocity, dt):
#     if isinstance(field, PointCloud):