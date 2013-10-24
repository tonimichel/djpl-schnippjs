from ape.installtools import cleanup, create_project_venv, fetch_pool, add_to_path
import os.path


# cleanup the installation directory (_lib/)
cleanup()
# create a project-level virtualenv
venv = create_project_venv()
# install some requirements
venv.pip_install_requirements('products/requirements.txt')
# add everything to your pypath
add_to_path(
    venv.get_paths(),
    os.path.dirname(os.path.abspath(__file__))
)







