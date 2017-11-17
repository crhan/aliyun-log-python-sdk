#!/usr/bin/env python
# encoding: utf-8

# Copyright (C) Alibaba Cloud Computing
# All rights reserved.

__all__ = ['CreateLogStoreResponse', 'DeleteLogStoreResponse', 'GetLogStoreResponse',
           'UpdateLogStoreResponse', 'ListLogStoreResponse']

from .util import Util
from .logresponse import LogResponse


class CreateLogStoreResponse(LogResponse):
    """ The response of the create_logstore API from log.
    
    :type header: dict
    :param header: CreateLogStoreResponse HTTP response header
    """

    def __init__(self, header, resp=''):
        LogResponse.__init__(self, header, resp)

    def log_print(self):
        print('CreateLogStoreResponse:')
        print('headers:', self.get_all_headers())


class DeleteLogStoreResponse(LogResponse):
    """ The response of the delete_logstore API from log.
    
    :type header: dict
    :param header: DeleteLogStoreResponse HTTP response header
    """

    def __init__(self, header, resp=''):
        LogResponse.__init__(self, header, resp)

    def log_print(self):
        print('DeleteLogStoreResponse:')
        print('headers:', self.get_all_headers())


class GetLogStoreResponse(LogResponse):
    """ The response of the get_logstore API from log.
    
    :type header: dict
    :param header: GetLogStoreResponse HTTP response header

    :type resp: dict
    :param resp: the HTTP response body
    """

    def __init__(self, resp, header):
        LogResponse.__init__(self, header, resp)
        self.logstore_name = Util.convert_unicode_to_str(resp["logstoreName"])
        self.ttl = int(resp["ttl"])
        self.shard_count = int(resp["shardCount"])

    def get_shard_count(self):
        """

        :return:
        """
        return self.shard_count

    def get_ttl(self):
        """

        :return:
        """
        return self.ttl

    def log_print(self):
        """

        :return:
        """
        print('GetLogStoreResponse:')
        print('headers:', self.get_all_headers())
        print('logstore_name:', self.logstore_name)
        print('shard_count:', str(self.shard_count))
        print('ttl:', str(self.ttl))


class UpdateLogStoreResponse(LogResponse):
    """ The response of the update_logstore API from log.
    
    :type header: dict
    :param header: UpdateLogStoreResponse HTTP response header
    """

    def __init__(self, header, resp=''):
        LogResponse.__init__(self, header, resp)

    def log_print(self):
        print('UpdateLogStoreResponse:')
        print('headers:', self.get_all_headers())


class ListLogStoreResponse(LogResponse):
    """ The response of the list_logstore API from log.
    
    :type header: dict
    :param header: ListLogStoreResponse HTTP response header

    :type resp: dict
    :param resp: the HTTP response body
    """

    def __init__(self, resp, header):
        LogResponse.__init__(self, header, resp)
        self.count = int(resp["count"])
        self.total_count = int(resp["total"])
        self.logstores = Util.convert_unicode_to_str(resp.get("logstores", []))

    def get_logstores(self):
        """

        :return:
        """
        return self.logstores

    def get_logstores_count(self):
        """

        :return:
        """
        return self.count

    def get_logstores_total(self):
        """

        :return:
        """
        return self.total_count

    def log_print(self):
        """

        :return:
        """
        print('ListLogStoreResponse:')
        print('headers:', self.get_all_headers())
        print('logstores_count:', str(self.count))
        print('logstores_total:', str(self.total_count))
        print('logstores:', str(self.logstores))