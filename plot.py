#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from rosbag import Bag
from rospy import Time
from datetime import datetime
from msgs import CarStatus
import matplotlib.pyplot as plt


def read_bag_file(bag_file_path):
    rtn = []
    try:
        msg: CarStatus
        t: Time
        with Bag(bag_file_path, "r") as bag:
            for topic, msg, t in bag.read_messages(
                topics=["/wheel_control/status_for_debug"]
            ):
                rtn.append((t.to_sec(), msg.phase_current_l, msg.phase_current_r))
    except Exception as e:
        print(f"Error reading bag file: {e}")

    return rtn


def plot_results(results):
    # Unzip the tuples into separate lists
    if not results:
        print("No data to plot.")
        return
    timestamps, phase_current_l, phase_current_r = zip(*results)

    # Convert Unix timestamps to human-readable datetime strings
    human_readable_timestamps = [
        datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S") for ts in timestamps
    ]

    plt.figure(figsize=(10, 5))
    plt.plot(human_readable_timestamps, phase_current_l, label="Phase Current L")
    plt.plot(human_readable_timestamps, phase_current_r, label="Phase Current R")
    plt.xlabel("Timestamp")
    plt.ylabel("Phase Current")
    plt.title("CarStatus Phase Currents Over Time")

    # Reduce the number of x-axis labels to avoid overlap
    plt.xticks(
        range(
            0,
            len(human_readable_timestamps),
            max(1, len(human_readable_timestamps) // 20),
        ),
        rotation=45,
        ha="right",
    )
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Read a ROS bag file and plot CarStatus messages."
    )
    parser.add_argument("bag_file_path", help="Path to the ROS bag file")
    parser.add_argument(
        "--phase-current",
        action="store_true",
        help="Plot phase current data",
        default=False,
    )
    args = parser.parse_args()

    if args.phase_current:
        results = read_bag_file(args.bag_file_path)
        plot_results(results)
