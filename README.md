Certainly! Here's a comprehensive README for your GitHub repository in both English and Persian, explaining the requirements and details of your code.

---

# AI Ecosystem Simulation

This repository contains a Python-based simulation of an AI-driven ecosystem. The simulation models organisms that move, eat, reproduce, and evolve over time.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Simulation Parameters](#simulation-parameters)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This simulation creates a virtual ecosystem where organisms interact with their environment. Each organism has a genome that dictates its behavior, and over time, they can evolve based on their success in surviving and reproducing.

## Requirements

- Python 3.6 or higher
- NumPy
- Matplotlib

## Installation

To run this simulation, you need to have Python and the necessary libraries installed. Follow the steps below:

1. Clone the repository:
    ```sh
    git clone https://github.com/mohsenakhavan/aiecology.git
    cd aiecology
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install numpy matplotlib
    ```

## Usage

Run the simulation using the following command:
```sh
python simulation.py
```

The simulation will display two plots:
1. A scatter plot showing the positions of organisms.
2. A line plot showing the population and average energy over generations.

## Simulation Parameters

- `WIDTH`, `HEIGHT`: Dimensions of the simulation grid.
- `INITIAL_POPULATION`: Initial number of organisms.
- `INITIAL_ENERGY`: Initial energy of each organism.
- `REPRODUCTION_THRESHOLD`: Energy threshold for reproduction.
- `REPRODUCTION_COST`: Energy cost of reproduction.
- `MUTATION_RATE`: Rate of mutation in the genome during reproduction.
- `MAX_AGE`: Maximum age of an organism.
- `MAX_FOOD`: Maximum amount of food available on the grid.
- `FOOD_GROWTH_RATE`: Rate of food regeneration.

## License

This project is licensed under the MIT License.

---

# شبیه‌سازی اکوسیستم هوش مصنوعی

این مخزن شامل شبیه‌سازی مبتنی بر پایتون از یک اکوسیستم هدایت شده توسط هوش مصنوعی است. شبیه‌سازی، ارگانیسم‌هایی را مدل‌سازی می‌کند که حرکت می‌کنند، می‌خورند، تولید مثل می‌کنند و با گذشت زمان تکامل می‌یابند.

## فهرست مطالب
- [مقدمه](#مقدمه)
- [پیش‌نیازها](#پیش‌نیازها)
- [نصب](#نصب)
- [استفاده](#استفاده)
- [پارامترهای شبیه‌سازی](#پارامترهای-شبیه‌سازی)
- [مشارکت](#مشارکت)
- [مجوز](#مجوز)

## مقدمه

این شبیه‌سازی یک اکوسیستم مجازی ایجاد می‌کند که در آن ارگانیسم‌ها با محیط خود تعامل دارند. هر ارگانیسم دارای ژنومی است که رفتار آن را دیکته می‌کند و با گذشت زمان، می‌توانند بر اساس موفقیت خود در بقا و تولید مثل تکامل یابند.

## پیش‌نیازها

- پایتون نسخه 3.6 یا بالاتر
- کتابخانه‌های NumPy و Matplotlib

## نصب

برای اجرای این شبیه‌سازی، باید پایتون و کتابخانه‌های مورد نیاز را نصب کرده باشید. مراحل زیر را دنبال کنید:

1. مخزن را کلون کنید:
    ```sh
    git clone https://github.com/mohsenakhavan/aiecology.git
    cd aiecology
    ```

2. یک محیط مجازی ایجاد و فعال کنید (اختیاری اما توصیه شده):
    ```sh
    python3 -m venv env
    source env/bin/activate  # در ویندوز از `env\Scripts\activate` استفاده کنید
    ```

3. بسته‌های مورد نیاز را نصب کنید:
    ```sh
    pip install numpy matplotlib
    ```

## استفاده

شبیه‌سازی را با استفاده از دستور زیر اجرا کنید:
```sh
python simulation.py
```

شبیه‌سازی دو نمودار را نمایش می‌دهد:
1. نمودار پراکندگی که موقعیت ارگانیسم‌ها را نشان می‌دهد.
2. نمودار خطی که جمعیت و میانگین انرژی را در نسل‌ها نشان می‌دهد.

## پارامترهای شبیه‌سازی

- `WIDTH`، `HEIGHT`: ابعاد شبکه شبیه‌سازی.
- `INITIAL_POPULATION`: تعداد اولیه ارگانیسم‌ها.
- `INITIAL_ENERGY`: انرژی اولیه هر ارگانیسم.
- `REPRODUCTION_THRESHOLD`: آستانه انرژی برای تولید مثل.
- `REPRODUCTION_COST`: هزینه انرژی تولید مثل.
- `MUTATION_RATE`: نرخ جهش در ژنوم هنگام تولید مثل.
- `MAX_AGE`: حداکثر سن یک ارگانیسم.
- `MAX_FOOD`: حداکثر مقدار غذا در شبکه.
- `FOOD_GROWTH_RATE`: نرخ بازسازی غذا.


## مجوز

این پروژه تحت مجوز MIT است.

---
