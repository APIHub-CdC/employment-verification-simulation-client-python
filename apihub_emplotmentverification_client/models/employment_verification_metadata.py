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


class EmploymentVerificationMetadata(object):
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
        'metadata': 'Metadata',
        'inquiries': 'list[EmploymentVerification]'
    }

    attribute_map = {
        'metadata': '_metadata',
        'inquiries': 'inquiries'
    }

    def __init__(self, metadata=None, inquiries=None):  # noqa: E501
        """EmploymentVerificationMetadata - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._inquiries = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if inquiries is not None:
            self.inquiries = inquiries

    @property
    def metadata(self):
        """Gets the metadata of this EmploymentVerificationMetadata.  # noqa: E501


        :return: The metadata of this EmploymentVerificationMetadata.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this EmploymentVerificationMetadata.


        :param metadata: The metadata of this EmploymentVerificationMetadata.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def inquiries(self):
        """Gets the inquiries of this EmploymentVerificationMetadata.  # noqa: E501


        :return: The inquiries of this EmploymentVerificationMetadata.  # noqa: E501
        :rtype: list[EmploymentVerification]
        """
        return self._inquiries

    @inquiries.setter
    def inquiries(self, inquiries):
        """Sets the inquiries of this EmploymentVerificationMetadata.


        :param inquiries: The inquiries of this EmploymentVerificationMetadata.  # noqa: E501
        :type: list[EmploymentVerification]
        """

        self._inquiries = inquiries

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
        if issubclass(EmploymentVerificationMetadata, dict):
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
        if not isinstance(other, EmploymentVerificationMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
