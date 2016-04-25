# Fundamentals 

- Unit tests check the behavoir of an element of code be it methods, or classes.
- Automated tests runs without interventions and reports results as either pass or fail.

It's not a unit test if it uses the file system, a database, or the network. Though the those tests can be useful, as integration 
tests. These tend to get a bit more complex.

## Why unit test
- Understand what to build - you should be able to write unit tests if you know what you are building, and if you cannot that means that 
you need to gain a better understanding.
- Design the units - Unit test help you decompose your code into units that are independently testable. Thus creating loose coupling. 
- Document the units - Tests document the behavior of the code, and how the unit is intented to be used.
- Regression protection - regression is where something used to work, and now it no longer works. Unit tests should be able to tell you if a 
portion of the code is no longer working becase of a change, therefore it makes sense to make the tests as good as possible to be able to tell
where the functionality is lost.

## Limitations
Unit testing cannot grantee that the software is 100% free of errors. In additoin there are things that unit tests cannot account for...
- Integration issues
- Security issues 
- Performance

## Test Last vs Test First vs Test Driven
- Test Last - You will end up discovering testablility problems and bugs late in the process. This can also cause you to have to skip tests because you have waited so long to test.
    - You right code
    - Then you invest in writing code
    - Debug and rework
    
- Test First - this forces you to write testable intefaces, though there is risk of rework. This reflects a waterfall like approach.
    - Design Code - create a rough interface for the code
    - Design Tests 
    - Write the code
    
- Test Driven 
    - Write test
    - Write little code
    - Refractor

## Three kinds of assertions 
- Check the return value or exception 
- Check a state change (public api)
- Check a method call (mock/spy)

## Monkeypatching 
this is where you change a peice of code at runtime. this is how to test code without testability in mind. 

##Vocabulary
- Test Double - this is a stand in for an actual class and the class that is using the class doesn't know that it isn't using the right thing.
    - Stub - test double that stands in for an object, same interface and no logic or advanced behavior
    - Fake - like a stub, except it contains logic and functionality for the purposes of the test. Useful for files, databases, and webservers.
    - Mock - likes stubs, returns hard coded values. The difference is that a mocks make assertions about an object, and can case the test to fail.
    - Test Spy - A spy records calls and then you can find out what happened from the spy calleds that were made and with what parameters. Spys do not fail they just record the results.

- TestCase - a test case is testing a specific portion of your system. The test case should be able to run independently of one another
 without any side effects. The name should be self explainitory. there are a few main parts to a test case
    - Name - this should be clear, and you should know what the module can do, and what functionality is broken if the test fails
        - Arrage - setup object to be tested=
        - Act - exercise the functionality of the object
        - Assert - make claims about the object, and collaborators
        - CleanUp -  Release resources, and restore the original state
    
 
- Test Runner - runs your tests, this can be represented as console or gui. The command for console is **python -m unittest**. 

- Test Suite - is a grouping of tests cases

- Test Fixture think set up, test case, and tear down. The set up will run before the test case to set up any dependencies, then the test case will run, finally tear down will clean up dependcies if necessary.

**Useful commands**
- python -m pytest
- python -m pytest -v
- python -m pytest --doctest-modules
- python -m pytest --doctest-modules -v