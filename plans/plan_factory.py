"""
William Geary
Student Loan Planner
27 July 2025
--------------------------------------------------------------------------------
plan_factory
"""

class PlanFactory:

    # Class methods
    @classmethod
    def get_plan(cls):
        """ Get a plan object given certain parameters """
        pass

    @classmethod
    def get_plan_from_json(cls):
        """ Get a plan object from a plan JSON object """
        pass

    # Helper methods
    @staticmethod
    def _create_plan(config):
        """ Create a plan object """
        plan_class = config.plan_type.plan_class
        return plan_class(config)