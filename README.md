# How to use SEMPRE

In this document, we will provide a brief memo how to read log files on SEMPRE and how to use it. The current version of SEMPRE is 2.1.

## What is SEMPRE?
SEMPRE is a toolkit for semantic parsers developed by a team leaded by Percy Liang.

[https://github.com/percyliang/sempre](https://github.com/percyliang/sempre)

SEMPRE is designed to quickly combine rule-based systems and machine learning-based systems learned from a set of utterance-denotation pairs and other forms of supervision.

Historically, the first version of SEMPRE 1.0 depends strongly on Freebase and its interface, [virtuoso](https://virtuoso.openlinksw.com). However, the updated version (>=2.0) focused on making it easy to develop semantic parses for new tasks. SEMPRE 2.1 is added `tables` and `overnight` packages for there new papers on ACL 2015.

## Usage of run command
The `run` script is the command-line interface for SEMPRE. We have to specify a running mode  from the following list:
```
Modes:
  test: Run unit tests
  freebase: Freebase (for EMNLP 2013, ACL 2014, TACL 2014)
  cacheserver: Start the general-purpose cache server that serves files with key-value maps
  filterfreebase: (1) Filter RDF Freebase dump (do this once) [takes about 1 hour]
  sparqlserver: (2) Start the SPARQL server [do this every time]
  indexfreebase: (3) Index the filtered RDF dump [takes 48 hours for Freebase]
  convertfree917: Convert the Free917 dataset
  query: Query a single logical form or SPARQL
  simple: Simple shell
  simple-sparql: Simple shell for querying SPARQL
  simple-lambdadcs: Simple shell for querying with the LambdaDCSExecutor
  simple-freebase: Simple shell for using Freebase
  simple-freebase-nocache: Simple shell for using Freebase (without a cache server)
  overnight: Overnight semantic parsing
  tables: QA on HTML tables
  genovernight: Generate utterances for overnight semantic parsing
  genovernight-wrapper: Generate utterances for overnight semantic parsing
  geo880: Semantic parsing on the geo880 dataset
```


We can use the `run` script for learning data, executing denotations, testing and others. Also we can specify [options](https://github.com/torotoki/howtouse-sempre/blob/master/RunningOptions.md)

## Testing with TestNG
We can run all unit tests in `edu.stanford.nlp.sempre.tests`:

```bash
./run @mode=test
```

Or We can run TestNG directly to specify detail options:
```bash
java -ea -Xmx12g -cp libsempre/*:lib/* org.testng.TestNG testng.xml
```

This should output passed/failed results at `test-output/index.html`, and also print out all logs on the test.

We can specify include/exclude tests on `testing.xml`:

### Testing specific methods
If we only want to test specific methods, we should specify the couple of methods belong to a new group:
```java
@Test(groups = {"nulltest"})
public void testMethod() {...}
```
Then, we should also specify this group to be included (or excluded) on `testng.xml`:
```xml
<groups>
  <run>
    <!-- <exclude name="grammar" /> -->`
  <include name="failingTest" />
  </run>
</groups>
```
