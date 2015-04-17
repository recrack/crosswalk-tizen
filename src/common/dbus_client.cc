// Copyright 2015 Samsung Electronics Co, Ltd. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "common/dbus_client.h"

#include "common/logger.h"

namespace wrt {

DBusClient::DBusClient()
    : connection_(NULL) {
}

DBusClient::~DBusClient() {
  if (connection_) {
    g_dbus_connection_close_sync(connection_, NULL, NULL);
  }
}

bool DBusClient::ConnectByName(const std::string& name) {
  std::string address("unix:path=");
  address.append(g_get_user_runtime_dir());
  address.append("/.");
  address.append(name);
  return Connect(address);
}

bool DBusClient::Connect(const std::string& address) {
  GError *err = NULL;
  connection_ = g_dbus_connection_new_for_address_sync(
      address.c_str(),
      G_DBUS_CONNECTION_FLAGS_AUTHENTICATION_CLIENT,
      NULL, NULL, &err);
  if (!connection_) {
    LoggerE("Failed to connect to bus address %s : %s",
           address.c_str(), err->message);
    g_error_free(err);
    return false;
  }
  return true;
}

GVariant* DBusClient::CallSync(const std::string& iface,
                               const std::string& method,
                               GVariant* parameters,
                               const GVariantType* reply_type) {
  if (!connection_) {
    return NULL;
  }

  GError *err = NULL;
  GVariant* reply = g_dbus_connection_call_sync(
      connection_, NULL, "/", iface.c_str(), method.c_str(), parameters,
      reply_type, G_DBUS_CALL_FLAGS_NONE, -1, NULL, &err);
  if (!reply) {
    LoggerE("Failed to CallSync : %s", err->message);
    g_error_free(err);
  }
  return reply;
}

}  // namespace wrt
