import sys, pathlib; sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from suppliersort_course.run_soar import run_soar_debugger

# Pick which files to run from this project folder
agent_file = "./_firstload_suppliersort.soar"
# agent_file = "./_firstload_instructor_solution.soar"

# Star Soar with a debugger using the indicated agent file
run_soar_debugger(agent_file)
