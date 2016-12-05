Panda3D test suite
==================

This directory contains a series of tests, written in Python using the unittest
framework, that test Panda3D through the Interrogate interfaces.

Each test can be run standalone. The files in the backends/ directories are NOT
runnable tests - they only serve as the test fixtures for a given subsystem
backend.

Tests for features not detected as enabled in your currently-installed version
of Panda3D will be skipped.
