diff --git a/clyent/__init__.py b/clyent/__init__.py
index 1fb3bda..855fe19 100644
--- a/clyent/__init__.py
+++ b/clyent/__init__.py
@@ -12,7 +12,6 @@ import sys
 
 from clyent.errors import ShowHelp
 
-from ._version import get_versions
 from .colors import print_colors
 
 class color(object):
@@ -155,5 +154,4 @@ def run_command(args, exit=True):
         else:
             return 1
 
-__version__ = get_versions()['version']
-del get_versions
+__version__ = '1.2.2'
diff --git a/setup.py b/setup.py
index 5bddfe6..175800f 100644
--- a/setup.py
+++ b/setup.py
@@ -1,10 +1,8 @@
 from setuptools import setup, find_packages
-import versioneer
 
 setup(
     name='clyent',
-    version=versioneer.get_version(),
-    cmdclass=versioneer.get_cmdclass(),
+    version='1.2.2',
     author='Continuum Analytics',
     author_email='srossross@gmail.com',
     url='http://github.com/binstar/clyent',
