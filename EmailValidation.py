{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMPn82oLwctiGKGi3doNXlx",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/er-surajgupta80484/PythonBasicProjects/blob/main/EmailValidation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BCS7TjUdiZOD",
        "outputId": "b5fed0dc-a8ad-4afa-e393-5f5ca4931756"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter email: surajgupta@12@gmail.com\n",
            "Email id cant have two @s\n"
          ]
        }
      ],
      "source": [
        "email=input(\"Enter email: \")\n",
        "count=0\n",
        "for i in email:\n",
        "  if i == '@':\n",
        "    count+=1\n",
        "if count==1:\n",
        "  if (email[-3]=='.')^ (email[-4]=='.'):\n",
        "    domain=email.split('@')\n",
        "    print(f\"User name is {domain[0]} and Domain is {domain[1]}\")\n",
        "  else:\n",
        "    print(\"Email id cant have two dots in domain name (.)\")\n",
        "else:\n",
        "  print(\"Email id should have one @ symbol\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Ztnm_5FfjeIJ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}