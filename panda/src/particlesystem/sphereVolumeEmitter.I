/**
 * PANDA 3D SOFTWARE
 * Copyright (c) Carnegie Mellon University.  All rights reserved.
 *
 * All use of this software is subject to the terms of the revised BSD
 * license.  You should have received a copy of this license along
 * with this source code in a file named "LICENSE."
 *
 * @file sphereVolumeEmitter.I
 * @author charles
 * @date 2000-06-26
 */

#include "config_particlesystem.h"

/**
 * radius set
 */

INLINE void SphereVolumeEmitter::
set_radius(PN_stdfloat r) {
  _radius = r;
}

/**
 * radius get
 */

INLINE PN_stdfloat SphereVolumeEmitter::
get_radius() const {
  return _radius;
}
