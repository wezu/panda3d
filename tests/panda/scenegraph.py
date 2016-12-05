#!/usr/bin/env python
import unittest
from .. import testbase

class TestNodePath(testbase.PandaTestCase):
    # Please keep tests sorted alphabetically!
    def test_empty(self):
        """Tests NodePath behavior for empty NodePaths."""
        from panda3d.core import NodePath

        empty = NodePath()
        self.assertTrue(empty.is_empty())

        self.assertEqual(empty.get_pos(), (0, 0, 0))
        self.assertEqual(empty.get_hpr(), (0, 0, 0))
        self.assertEqual(empty.get_scale(), (1, 1, 1))

    def test_parent(self):
        """Tests NodePath.reparentTo()."""
        from panda3d.core import NodePath

        np1 = NodePath()
        np2 = NodePath()

        self.assertTrue(np1.get_parent().is_empty())
        self.assertTrue(np2.get_parent().is_empty())

        np1.reparentTo(np2)

        self.assertEqual(np1.get_parent(), np2)
        self.assertTrue(np2.get_parent().is_empty())

    def test_transform_changes(self):
        """Tests that NodePath applies transform changes to its managed node."""
        from panda3d.core import NodePath

        np = NodePath('np')
        self.assertEqual(np.get_pos(), (0, 0, 0))
        self.assertEqual(np.get_hpr(), (0, 0, 0))
        self.assertEqual(np.get_scale(), (1, 1, 1))

        np.set_pos(1, 2, 3)
        self.assertEqual(np.get_pos(), (1, 2, 3))
        self.assertEqual(np.node().get_transform().get_pos(), (1, 2, 3))

    def test_transform_composition(self):
        """Tests that NodePath composes transform states according to the path it holds."""
        from panda3d.core import PandaNode, NodePath, Point3, Vec3

        # Create 3 PandaNodes, and give each some interesting transform state:
        node1 = PandaNode('node1')
        node2 = PandaNode('node2')
        node3 = PandaNode('node3')

        node1.set_transform(node1.get_transform().set_pos(Point3(0, 0, 1)).set_hpr(Vec3(90, 0, -90)))
        node2.set_transform(node2.get_transform().set_pos(Point3(0, 1, 0)).set_hpr(Vec3(180, 180, 0)))
        node3.set_transform(node3.get_transform().set_pos(Point3(1, 0, 0)).set_hpr(Vec3(270, 0, 270)))

        # node3 is going to be attached under both node1 and node2 and we will
        # hold a path both ways:
        node1.add_child(node3)
        node2.add_child(node3)

        self.assertEqual(node1.get_num_children(), 1)
        self.assertEqual(node2.get_num_children(), 1)
        self.assertEqual(node3.get_num_children(), 0)
        self.assertEqual(node1.get_num_parents(), 0)
        self.assertEqual(node2.get_num_parents(), 0)
        self.assertEqual(node3.get_num_parents(), 2)

        # np1 is the path to node3 via node1:
        np1 = NodePath(node1).get_child(0)
        # np2 is the path to node3 via node2:
        np2 = NodePath(node2).get_child(0)

        # Both should point to node3:
        self.assertEqual(np1.node(), node3)
        self.assertEqual(np2.node(), node3)

        # However if we ask for the net transform to node3, it should compose:
        self.assertEqual(np1.get_transform(NodePath()),
                               node1.get_transform().compose(node3.get_transform()))
        self.assertEqual(np2.get_transform(NodePath()),
                               node2.get_transform().compose(node3.get_transform()))

        # If we ask for np1 RELATIVE to np2, it should compose like so:
        leg1 = node2.get_transform().compose(node3.get_transform())
        leg2 = node1.get_transform().compose(node3.get_transform())
        relative_transform = leg1.get_inverse().compose(leg2)
        self.assertEqual(np1.get_transform(np2), relative_transform)


if __name__ == '__main__':
    unittest.main()
