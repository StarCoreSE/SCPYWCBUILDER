        WeaponDefinition LargeBlockArtillery => new WeaponDefinition
        {
            Assignments = new ModelAssignmentsDef
            {
                MountPoints = new[] {
                    new MountPointDef {
                        SubtypeId = "LargeBlockLargeCalibreGun", 
                        MuzzlePartId = "None", 
                        AzimuthPartId = "None", 
                        ElevationPartId = "None",
                    },
                    
                 },
                Muzzles = new[] {
                    "muzzle_missile_001",
                },
            },            
            Targeting = new TargetingDef //Note this is used by the CTC
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
                PartName = "Artillery", 
                DeviateShotAngle = 0.15f,
                AimingTolerance = 2f,
                HardWare = new HardwareDef
                {
                    InventorySize = 0.3f,
                    Type = BlockWeapon,
                },
                Loading = new LoadingDef
                {
                    RateOfFire = 80,
                    BarrelsPerShot = 1,
                    TrajectilesPerBarrel = 1,
                    ReloadTime = 720,
                    MagsToLoad = 1,
                },
                Audio = new HardPointAudioDef
                {
                    FiringSound = "WepLargeCalibreShot",
                    FiringSoundPerShot = true,
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