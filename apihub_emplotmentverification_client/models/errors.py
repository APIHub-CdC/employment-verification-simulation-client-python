# coding: utf-8

"""
    API Employment Verification Sandbox

    This API lets you verify a person employment status. If a person has a job it also returns the industrial sector and the industry COVID risk segment.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: api@circulodecredito.com.mx
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Errors(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'errors': 'list[Error]'
    }

    attribute_map = {
        'errors': 'errors'
    }

    def __init__(self, errors=None):  # noqa: E501
        """Errors - a model defined in Swagger"""  # noqa: E501

        self._errors = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors

    @property
    def errors(self):
        """Gets the errors of this Errors.  # noqa: E501

        List of errors.  # noqa: E501

        :return: The errors of this Errors.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Errors.

        List of errors.  # noqa: E501

        :param errors: The errors of this Errors.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Errors, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Errors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
