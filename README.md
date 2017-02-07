# How to use SEMPRE

In this document, we will provide a brief memo how to read log files on SEMPRE and how to use it.

## What is SEMPRE?
SEMPRE is a toolkit for semantic parsers developed by a team leaded by Percy Liang.

[https://github.com/percyliang/sempre](https://github.com/percyliang/sempre)

Historically, the first version of SEMPRE 1.0 depends strongly on Freebase and its interface, [virtuoso](https://virtuoso.openlinksw.com). However, the updated version (>=2.0) focused on making it easy to develop semantic parses for new tasks. One can quickly combine rule-based systems and machine learning-based system learned from a set of utterance-denotation pairs and other forms of supervision.

## Usage of run command
The `run` script is the command-line interface for SEMPRE. You can use it for learning data, executing denotations, testing and others.

```
Usage: <main class> [options] The XML suite files to run
  Options:
    -configfailurepolicy
       Configuration failure policy (skip or continue)
    -d
       Output directory
    -dataproviderthreadcount
       Number of threads to use when running data providers
    -excludegroups
       Comma-separated list of group names to  exclude
    -groups
       Comma-separated list of group names to be run
    -junit
       JUnit mode
       Default: false
    -listener
       List of .class files or list of class names implementing ITestListener or
       ISuiteListener
    -methods
       Comma separated of test methods
       Default: []
    -methodselectors
       List of .class files or list of class names implementing IMethodSelector
    -mixed
       Mixed mode - autodetect the type of current test and run it with
       appropriate runner
       Default: false
    -objectfactory
       List of .class files or list of class names implementing
       ITestRunnerFactory
    -parallel
       Parallel mode (methods, tests or classes)
    -port
       The port
    -reporter
       Extended configuration for custom report listener
    -suitename
       Default name of test suite, if not specified in suite definition file or
       source code
    -suitethreadpoolsize
       Size of the thread pool to use to run suites
       Default: 1
    -testclass
       The list of test classes
    -testjar
       A jar file containing the tests
    -testname
       Default name of test, if not specified in suitedefinition file or source
       code
    -testnames
       The list of test names to run
    -testrunfactory, -testRunFactory
       The factory used to create tests
    -threadcount
       Number of threads to use when running tests in parallel
    -usedefaultlisteners
       Whether to use the default listeners
       Default: true
    -log, -verbose
       Level of verbosity
    -xmlpathinjar
       The full path to the xml file inside the jar file (only valid if -testjar
       was specified)
       Default: testng.xml

```

## Testing with TestNG
We can execute all tests in `edu.stanford.nlp.sempre.tests`:

```bash
./run @mode=test
```

Or you can use a fast-check option which excludes sparql and corenlp tests:
```bash
./run @mode=test -fast
```

This should output passed/failed results at `test-output/index.html`, and also print out all logs in the test.
