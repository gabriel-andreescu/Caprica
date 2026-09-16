#pragma once

#include <cassert>

#include <atomic>
#include <condition_variable>
#include <exception>
#include <mutex>
#include <thread>
#include <vector>

namespace caprica {

struct CapricaJob abstract {
  CapricaJob() = default;
  CapricaJob(const CapricaJob& other) = delete;
  CapricaJob(CapricaJob&& other) = delete;
  CapricaJob& operator=(const CapricaJob&) = delete;
  CapricaJob& operator=(CapricaJob&&) = delete;
  ~CapricaJob() = default;

  void await();
  bool hasRun();

protected:
  virtual void run() = 0;

private:
  std::atomic<bool> hasRan { false };
  std::atomic<bool> runningLock { false };
  std::condition_variable ranCondition;
  std::mutex ranMutex;
  std::exception_ptr failure;

  friend struct CapricaJobManager;
  std::atomic<CapricaJob*> next { nullptr };

  bool tryRun();
};

struct CapricaJobManager final {
  ~CapricaJobManager();
  void startup(size_t workerCount);
  // Wait for all workers to shutdown
  void awaitShutdown();
  bool tryDeque(CapricaJob** retJob);
  void queueJob(CapricaJob* job);

  void setQueueInitialized() { queueInitialized.store(true, std::memory_order_relaxed); }
  // Run the currently executing thread as
  // a worker.
  void enjoin();

private:
  struct DefaultJob final : public CapricaJob {
    virtual void run() override { }
  } defaultJob;
  std::atomic<CapricaJob*> front { &defaultJob };
  std::atomic<CapricaJob*> back { &defaultJob };
  std::vector<std::thread> workers;
  std::mutex failureMutex;
  std::exception_ptr failure;
  std::condition_variable queueCondition;
  std::atomic<size_t> queuedItemCount { 0 };
  std::atomic<size_t> waiterCount { 0 };
  std::atomic<size_t> workerCount { 0 };
  std::atomic<bool> stopWorkers { false };
  std::atomic<bool> queueInitialized { false };

  void workerMain();
};

}
