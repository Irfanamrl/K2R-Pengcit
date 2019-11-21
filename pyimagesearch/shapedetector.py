{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "outputs": [],
   "source": [
    "# import the necessary packages\n",
    "import cv2\n",
    "\n",
    "class ShapeDetector:\n",
    "    def __init__(self):\n",
    "        pass\n",
    "    \n",
    "    def detect(self, c):\n",
    "        # initialize the shape name and approximate the contour\n",
    "        shape = 'unindentified'\n",
    "        peri = cv2.arcLength(c,True)\n",
    "        approx = cv2.approxPlyDP(c, 0.04 * peri, True)\n",
    "        \n",
    "        #if \n",
    "        "
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n",
     "is_executing": false
    }
   }
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  },
  "pycharm": {
   "stem_cell": {
    "cell_type": "raw",
    "source": [],
    "metadata": {
     "collapsed": false
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}