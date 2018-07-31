test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.color
          'No color yet. You need to paint me.'
          >>> hilfingers_car.paint('black')
          'Tesla Model S is now black'
          >>> hilfingers_car.color
          'black'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.model
          'Model S'
          >>> hilfingers_car.gas = 10
          >>> hilfingers_car.drive()
          'Tesla Model S goes vroom!'
          >>> hilfingers_car.drive()
          'Tesla Model S cannot drive!'
          >>> hilfingers_car.fill_gas()
          'Tesla Model S gas level: 20'
          >>> hilfingers_car.gas
          20
          >>> Car.gas
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> Car.headlights
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> hilfingers_car.headlights
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> Car.headlights = 3
          >>> hilfingers_car.headlights
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          >>> hilfingers_car.headlights = 2
          >>> Car.headlights
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.wheels = 2
          >>> hilfingers_car.wheels
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> Car.num_wheels
          612ff2a71cad53bc4c7f85fac678a06d
          # locked
          >>> hilfingers_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          8e18dc54497447151e91747068c581ce
          # locked
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          8a2fd4e4c3c6dcce2dc631af62ee217a
          # locked
          >>> Car.drive(hilfingers_car) # Type Error if an error occurs and Nothing if nothing is displayed
          8e18dc54497447151e91747068c581ce
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
