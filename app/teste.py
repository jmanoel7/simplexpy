import qsoptex
import logging

logging.basicConfig(level=logging.DEBUG)

p = qsoptex.ExactProblem()

p.add_variable(name='x', objective=2, lower=3.5, upper=17.5)
p.add_variable(name='y', objective=-1, lower=None, upper=2)
p.add_linear_constraint(qsoptex.ConstraintSense.EQUAL,
                                {'x': 1, 'y': 1}, rhs=0)
p.set_objective_sense(qsoptex.ObjectiveSense.MAXIMIZE)

p.set_param(qsoptex.Parameter.SIMPLEX_DISPLAY, 1)
status = p.solve()
if status == qsoptex.SolutionStatus.OPTIMAL:
    print('Optimal solution')
    print(p.get_objective_value())
    print(p.get_value('x'))
