AppVersion is a library that can fetch app version from playstore or appstore.
You only need to prepare the package name or bundle id as argument.
also It has various util function for calculate version.

# Install
```shell script
pip install appversion
```

# Quick start
```python
from av import AppVersion

# arg - android package name.
playstore_version = AppVersion.playstore('com.youjinui.endword')
print(playstore_version) # 1.2.1

# arg - iOS bundle id.
appstore_version = AppVersion.appstore('com.youjinui.endword')
print(appstore_version) # 1.0.0
```

# Calculate version
## Max
This function return max version from two arguments. 
```python
from av import AppVersion

max_version = AppVersion.maxv('0.0.1', '0.0.2')
print(max_version)
```
return `0.0.2`

## Min
This function return min version from two arguments.
```python
from av import AppVersion

min_version = AppVersion.minv('1.0.a', '1.0.b')
print(min_version)
```
return `1.0.a`

## Equals
This function returns a boolean value of whether the version are equals or different.
```python
from av import AppVersion

is_equal = AppVersion.equals('1.1', '1.1.0.0.0')
print(is_equal)
```
return `True`

## Compare
This function returns a boolean value of whether the arg1 is greater than arg2. 
```python
from av import AppVersion

is_arg1_greater_than_arg2 = AppVersion.compare('1.1.12', '1.1.3')
print(is_arg1_greater_than_arg2)
```
return `True`


# Authors
tinyjin - [Github](https://github.com/tinyjin), [Blog](https://wlsdml1103.blog.me)

# License
This library has MIT License.
