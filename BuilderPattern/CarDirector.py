from Director import Director

class CarDirector(Director):
    # The car director follows its own sequence:
    # Make body-> add wheels-> then add the brand name.
    def instruct(self, builder):
        builder.build_body()
        builder.insert_wheels()
        builder.add_brand_name()
        return builder.get_vehicle()