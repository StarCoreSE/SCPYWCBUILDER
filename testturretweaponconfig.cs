WeaponDefinition LargeBlockArtilleryTurret => new WeaponDefinition
        {
            Assignments = new ModelAssignmentsDef
            {
                MountPoints = new[] {
                    new MountPointDef {
                        SubtypeId = "LargeCalibreTurret",
                        MuzzlePartId = "MissileTurretBarrels",
                        AzimuthPartId = "MissileTurretBase1", 
                        ElevationPartId = "MissileTurretBarrels",
                    },                  
                 },
                Muzzles = new[] {
                    "muzzle_missile_001",
                },
            },
            Targeting = new TargetingDef
            {
                Threats = new[] {
                    Grids,
                },
                SubSystems = new[] {
                    Power, Utility, Offense, Thrust, Production, Any, 
                },
            },
            HardPoint = new HardPointDef
            {
                PartName = "Artillery Turret",
                DeviateShotAngle = 0.3f, 
                AimingTolerance = 2f, 
                AimLeadingPrediction = Advanced, 
                Ai = new AiDef
                {
                    TrackTargets = true,
                    TurretAttached = true,
                    TurretController = true,
                },
                HardWare = new HardwareDef
                {
                    RotateRate = 0.005f,
                    ElevateRate = 0.005f,
                    MinAzimuth = -180,
                    MaxAzimuth = 180,
                    MinElevation = -15,
                    MaxElevation = 60,
                    InventorySize = 0.6f,
                    Type = BlockWeapon,
                },
                Loading = new LoadingDef
                {
                    RateOfFire = 697,
                    BarrelsPerShot = 1,
                    TrajectilesPerBarrel = 1,
                    ReloadTime = 1545,
                    MagsToLoad = 1,
                },
                Audio = new HardPointAudioDef
                {
                    FiringSound = "WepLargeCalibreShot",
                    FiringSoundPerShot = true,
                    HardPointRotationSound = "WepTurretGatlingRotate",
                },
                Graphics = new HardPointParticleDef
                {
                    Effect1 = new ParticleDef
                    {
                        Name = "Muzzle_Flash_LargeCalibre",
                        Extras = new ParticleOptionDef
                        {
                            Scale = 1f,
                        },
                    },
                },
            },
            Ammos = new[] {
                ArtilleryShell,
            },
        };