import itk
import faulthandler

faulthandler.enable()
fixed_image = itk.imread('data/CT_2D_head_fixed.mha', itk.F)
moving_image = itk.imread('data/CT_2D_head_moving.mha', itk.F)

parameter_object = itk.ParameterObject.New()
default_rigid_parameter_map = parameter_object.GetDefaultParameterMap('rigid')
parameter_object.AddParameterMap(default_rigid_parameter_map)

result_image, result_transform_parameters = itk.elastix_registration_method(
    fixed_image, moving_image,
    parameter_object=parameter_object,
    log_to_console=False)
