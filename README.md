### Network Security – Phishing URL Detection App

This project is a Python-based network security application that uses Machine Learning to detect and classify suspicious or phishing URLs. The goal is to provide an early warning system that helps users and organizations avoid malicious websites that could lead to data theft, fraud, or malware infections.

The model is trained on a dataset of engineered URL and domain-level features such as IP usage, URL length, HTTPS tokens, domain age, DNS records, redirection behavior, and several browser-based indicators. Each feature is numerically encoded to represent whether a characteristic is safe, suspicious, or malicious, enabling efficient model training and fast real-time predictions.

Key Features

Phishing Detection: Classifies URLs as legitimate or malicious.

Feature-Driven Analysis: Uses multiple security indicators instead of relying on a single rule.

Machine Learning Powered: Trained on labeled data for better generalization.

Lightweight & Fast: Designed to run quickly for near real-time checks.

Extensible Architecture: New features or models can be added easily.