from Director import Director

class MotorCycleDirector(Director):
    # The motor cycle director follows its own sequence:
    # Add brand name-> make body-> insert wheels.
    def instruct(self, builder):
        builder.add_brand_name()
        builder.build_body()
        builder.insert_wheels()
        return builder.get_vehicle()