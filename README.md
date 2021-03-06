Humilis plug-in to deploy a security groups in a security
====================================================

[![PyPI](https://img.shields.io/pypi/v/humilis-security.svg?style=flat)](https://pypi.python.org/pypi/humilis-security)

A [humilis][humilis] plug-in layer to deploy security groups in a [VPC][vpc].

[vpc]: https://aws.amazon.com/vpc/
[humilis]: https://github.com/humilis/humilis


## Installation


```
pip install humilis-security
```


To install the development version:

```
pip install git+https://github.com/humilis/humilis-security
```


## Development

Assuming you have [virtualenv][venv] installed:

[venv]: https://virtualenv.readthedocs.org/en/latest/

```
make develop
```

Configure humilis:

```
make configure
```


## Testing

You can test the deployment of a sample of security groups with:

```
make test
```

The test suite should destroy the created resources automatically, but you
can make sure you are not leaving any infrastructure behind by manually
running:

```bash
make delete
```


## More information

See [humilis][humilis] documentation.



## Contact

If you have questions, bug reports, suggestions, etc. please create an issue on
the [GitHub project page][github].

[github]: http://github.com/humilis/humilis-security


## License

This software is licensed under the [MIT license][mit].

[mit]: http://en.wikipedia.org/wiki/MIT_License

See [License file][LICENSE].

[LICENSE]: https://github.com/humilis/humilis-security/blob/master/LICENSE.txt


© 2016 German Gomez-Herrero, [Find Hotel][fh] and others.

[fh]: http://company.findhotel.net
