// Copyright (c) 2018-2019 Zededa, Inc.
// SPDX-License-Identifier: Apache-2.0

// Routines which operate on types.GlobalConfig

package utils

import (
	"os"
	"io/ioutil"
	"strconv"

	"github.com/lf-edge/eve/pkg/pillar/base"
	"github.com/lf-edge/eve/pkg/pillar/pubsub"
	pubsublegacy "github.com/lf-edge/eve/pkg/pillar/pubsub/legacy"
	"github.com/lf-edge/eve/pkg/pillar/types"
)

const (
	globalConfigDir = types.PersistConfigDir + "/ConfigItemValueMap"
	symlinkDir      = types.TmpDirname + "/ConfigItemValueMap"
)

// EnsureGCFile is used by agents which wait for GlobalConfig to become initialized
// on startup in order to make sure we have a GlobalConfig file.
func EnsureGCFile(log *base.LogObject) {
	pubGlobalConfig, err := pubsublegacy.PublishPersistent("", types.ConfigItemValueMap{})
	if err != nil {
		log.Fatal(err)
	}
	ReadAndUpdateGCFile(log, pubGlobalConfig)
}

// CreateSymlink - Creates Symbolic link:
//  linkDir -->targetDir
func CreateSymlink(log *base.LogObject, linkDir, targetDir string) {
	// Make sure we have a correct symlink from /var/tmp/zededa so
	// others can subscribe from there
	log.Debugf("CreateSymlink")
	info, err := os.Lstat(linkDir)
	if err == nil {
		if (info.Mode() & os.ModeSymlink) != 0 {
			log.Debugf("CreateSymlink - symlink already exists")
			return
		}
		log.Warnf("CreateSymlink - Removing old %s", symlinkDir)
		if err := os.RemoveAll(linkDir); err != nil {
			log.Fatal(err)
		}
	}
	log.Debugf("CreateSymlink - Creating symlink")
	if err := os.Symlink(targetDir, linkDir); err != nil {
		log.Fatalf("CreateSymlink: Failed to create symlink %s -> %s . Err: %s",
			linkDir, targetDir, err)
	}
}

// ReadAndUpdateGCFile does the work of getting a sane or default
// GlobalConfig based on the current definition of GlobalConfig which
// might be different than the file stored on disk if we did an update
// of EVE.
func ReadAndUpdateGCFile(log *base.LogObject, pub pubsub.Publication) {
	key := "global"
	item, err := pub.Get(key)
	if err == nil {
		gc := item.(types.ConfigItemValueMap)
		err := pub.Publish(key, gc)
		if err != nil {
			log.Errorf("Publish for globalConfig failed: %s",
				err)
		}

	} else {
		log.Warn("No globalConfig in /persist; creating it with defaults")
		err := pub.Publish(key, *types.DefaultConfigItemValueMap())
		if err != nil {
			log.Errorf("Publish for globalConfig failed %s\n",
				err)
		}
	}
	CreateSymlink(log, symlinkDir, globalConfigDir)
}

// RoundToMbytes - Byts convert to Mbytes with round-off
func RoundToMbytes(byteCount uint64) uint64 {
	const mbyte = 1 << 20

	return (byteCount + mbyte/2) / mbyte
}

func SetOomScore(pid int, oomScore int32) error {
	filename := "/proc/" + strconv.Itoa(pid) + "/oom_score_adj"
	oomScoreStr := strconv.Itoa(int(oomScore))

	return ioutil.WriteFile(filename, []byte(oomScoreStr), 0600)
}

